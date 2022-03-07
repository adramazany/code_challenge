package com.challenge.sharenow;
/*
 * @created 3/7/2022 - 8:20 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */
import com.challenge.sharenow.model.Vehicle;
import org.junit.jupiter.api.Test;

import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;
import java.util.HashMap;
import java.util.function.Function;
import java.util.stream.Collectors;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
public class TestVehicleAPI {

    @Test
    void testGetVehicles(){
        RestTemplate restTemplate = new RestTemplate();
        String location="Stuttgart";
        String url="http://localhost:3000/vehicles/"+location;
        ResponseEntity<Vehicle[]> response =restTemplate.getForEntity(url,Vehicle[].class);
        assertEquals(response.getStatusCode().is2xxSuccessful(),true);
        Vehicle[] vehicles = response.getBody();
        System.out.println("vehicles.length=" +vehicles.length);
//        assertThat(foo.getName(), notNullValue());
//        assertThat(foo.getId(), is(1L));

    }

    @Test
    void testPutToMap() {
        HashMap<String, Vehicle> vehicles = new HashMap<>();

        RestTemplate restTemplate = new RestTemplate();
        String location = "Stuttgart";
        String url = "http://localhost:3000/vehicles/" + location;
        ResponseEntity<Vehicle[]> response = restTemplate.getForEntity(url, Vehicle[].class);
        if (response.getStatusCode().is2xxSuccessful()) {
            Vehicle[] resVehicles = response.getBody();
            System.out.println("resVehicles.length=" +resVehicles.length);
            vehicles.putAll(
                    Arrays.stream(resVehicles).collect(
                            Collectors.toMap(Vehicle::getVin, Function.identity(), (existing, replacement) -> replacement)
                    )
            );
            System.out.println("vehicles.size=" +vehicles.size());
            System.out.println("vehicles=" +vehicles);
        }

        //second time - must not duplicate
        response = restTemplate.getForEntity(url, Vehicle[].class);
        if (response.getStatusCode().is2xxSuccessful()) {
            Vehicle[] resVehicles = response.getBody();
            System.out.println("resVehicles.length=" +resVehicles.length);
            vehicles.putAll(
                    Arrays.stream(resVehicles).collect(
                            Collectors.toMap(Vehicle::getVin, Function.identity(), (existing, replacement) -> replacement)
                    )
            );
            System.out.println("vehicles.size=" +vehicles.size());
            System.out.println("vehicles=" +vehicles);
        }
        //third time - must not duplicate
        response = restTemplate.getForEntity(url, Vehicle[].class);
        if (response.getStatusCode().is2xxSuccessful()) {
            Vehicle[] resVehicles = response.getBody();
            System.out.println("resVehicles.length=" +resVehicles.length);
            vehicles.putAll(
                    Arrays.stream(resVehicles).collect(
                            Collectors.toMap(Vehicle::getVin, Function.identity(), (existing, replacement) -> replacement)
                    )
            );
            System.out.println("vehicles.size=" +vehicles.size());
            System.out.println("vehicles=" +vehicles);
        }
    }

}
