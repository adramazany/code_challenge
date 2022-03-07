package com.challenge.sharenow.controller;
/*
 * @created 3/7/2022 - 12:06 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.challenge.sharenow.exception.VehicleNotFoundException;
import com.challenge.sharenow.model.Vehicle;
import com.challenge.sharenow.repository.PolygonRepository;
import com.challenge.sharenow.repository.VehicleRepository;
import com.challenge.sharenow.service.AdminService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/vehicles")
public class VehicleAPI {

    @Autowired
    VehicleRepository vehicleRepository;

    @GetMapping("/")
    Vehicle[] all(){
        return vehicleRepository.findAll();
    }


    @GetMapping("/{vin}")
    Vehicle one(@PathVariable String vin){
        return vehicleRepository.findByVin(vin);
    }




}
