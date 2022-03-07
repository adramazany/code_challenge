package com.challenge.sharenow.repository;
/*
 * @created 3/6/2022 - 11:51 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 *
 * for now we store data in memory
 */

import com.challenge.sharenow.model.Vehicle;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

@Component
public class VehicleRepository {
    HashMap<String,Vehicle> vehicles = new HashMap<>();

    public HashMap<String, Vehicle> getVehicles() {
        return vehicles;
    }

    public void setVehicles(HashMap<String, Vehicle> vehicles) {
        this.vehicles = vehicles;
    }
}
