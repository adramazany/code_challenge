package com.challenge.sharenow.service;
/*
 * @created 3/6/2022 - 11:51 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.challenge.sharenow.model.GeoPolygon;
import com.challenge.sharenow.model.Vehicle;
import com.challenge.sharenow.repository.PolygonRepository;
import com.challenge.sharenow.repository.VehicleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

@Service
public class GeoService {

    @Autowired
    VehicleRepository vehicleRepository;

    @Autowired
    PolygonRepository polygonRepository;

    @Autowired
    RestTemplate restTemplate;

    @Value("${sharenow.vehicles_url}")
    String vehicles_url;

    public void refreshVehicles(String location){
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<Vehicle[]> response =restTemplate.getForEntity(vehicles_url+location,Vehicle[].class);
        if(response.getStatusCode().is2xxSuccessful()){
//          Get Exist Vehicles
            HashMap<String,Vehicle> existsVehicles = vehicleRepository.getVehicles();
//          Returened vehicles from API
            Vehicle[] resVehicles = response.getBody();
//          Find Vehicle in last polygon and remove it from polygon's VINs
            for (Vehicle v:resVehicles) {
                Vehicle existVehicle =  existsVehicles.get(v.getVin());
                if(existVehicle!=null && existVehicle.getPolygonId()!=null){
                    GeoPolygon lastPolygon = polygonRepository.findById(existVehicle.getPolygonId());
                    if(lastPolygon!=null){
                        lastPolygon.removeVin(v.getVin());
                    }
                }
            }
//          Find every vehicle's polygon and add vehicle to polygon vins
//            Arrays.stream(resVehicles).forEach(v->v.setGeoPolygon( polygonRepository.findByLngLat(v.getPosition()) ));
            List<Vehicle> geoVehicles = Arrays.stream(resVehicles).map(
                    v -> {
                        GeoPolygon geoPolygon = polygonRepository.findIdByLngLat(v.getPosition());
                        if(geoPolygon!=null){
                            v.setPolygonId( geoPolygon.get_id() );
                            geoPolygon.addVin(v.getVin());
                        }
                        return v;})
                    .collect(Collectors.toList());
            existsVehicles.putAll(geoVehicles.stream().collect(
                    Collectors.toMap(Vehicle::getVin, Function.identity(), (existing, replacement) -> replacement)));
            vehicleRepository.setVehicles(existsVehicles);// It just for future usage
        }
    }


}
