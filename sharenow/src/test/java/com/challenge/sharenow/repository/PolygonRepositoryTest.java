package com.challenge.sharenow.repository;

import com.challenge.sharenow.model.GeoPolygon;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/*
 * @created 3/7/2022 - 7:40 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

@SpringBootTest
class PolygonRepositoryTest {

    @Autowired
    PolygonRepository polygonRepository;

    @Test
    void getGeoPolygons() {
        HashMap<String,GeoPolygon> geoPolygons =polygonRepository.getGeoPolygons();
        assertEquals(geoPolygons.size(),154);
    }

    @Test
    void findByLongLat() throws IOException {
        double longitude = 9.32108402253,latitude=48.7508977740;
        GeoPolygon geoPolygon = polygonRepository.findByLngLat(longitude,latitude);
        assertNotNull(geoPolygon);
    }
}