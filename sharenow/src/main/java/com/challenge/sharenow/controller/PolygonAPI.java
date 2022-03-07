package com.challenge.sharenow.controller;
/*
 * @created 3/7/2022 - 12:06 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.challenge.sharenow.model.GeoPolygon;
import com.challenge.sharenow.model.Vehicle;
import com.challenge.sharenow.repository.PolygonRepository;
import com.challenge.sharenow.repository.VehicleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/geo/polygons")
public class PolygonAPI {

    @Autowired
    PolygonRepository polygonRepository;

    @GetMapping("/")
    GeoPolygon[] all(){
        return polygonRepository.findAll();
    }

    @GetMapping("/{id}")
    GeoPolygon one(@PathVariable String id){
        return polygonRepository.findById(id);
    }

}
