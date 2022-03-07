package com.challenge.sharenow.repository;
/*
 * @created 3/6/2022 - 11:51 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 *
 * for now we store data in memory
 */

import com.challenge.sharenow.model.Vehicle;
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.List;

@Component
public class VehicleRepository {
    HashMap<String,Vehicle> vehicles = new HashMap<>();

    public HashMap<String, Vehicle> getVehicles() {
        return vehicles;
    }

    public void setVehicles(HashMap<String, Vehicle> vehicles) {
        this.vehicles = vehicles;
    }

    public Vehicle findByVin(String vin){
        return vehicles.get(vin);
    }

    public Vehicle[] findAll(){
        return vehicles.values().toArray(Vehicle[]::new);
    }
}
