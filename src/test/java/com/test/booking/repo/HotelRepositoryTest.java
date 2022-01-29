package com.test.booking.repo;

import com.test.booking.config.BookingConfiguration;
import com.test.booking.model.City;
import com.test.booking.model.Hotel;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ContextConfiguration;

import java.util.Iterator;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/*
 * @created 1/26/2022 - 12:39 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

@SpringBootTest
@ContextConfiguration(classes = com.test.booking.config.BookingConfiguration.class)
class HotelRepositoryTest {
    Logger logger = LoggerFactory.getLogger(HotelRepositoryTest.class);

    @Autowired
    HotelRepository hotelRepository;

    @Test
    void testListHotel(){
        Iterable<Hotel> hotels = hotelRepository.findAll();

        logger.info("testListHotel: {}",hotels);
    }

    @Test
    void testUpdate(){
        Hotel hotel = new Hotel();
        hotel.setHotelId(1);
        hotel.setCity(new City(1));
        hotel.setRate(1);
        hotel.setName("hotel11");
        hotelRepository.update(hotel);
        logger.info("update done. {}",hotel);
    }

    @Test
    void testFindByCityId(){
        List<Hotel> hotels = hotelRepository.findByCityId(1);
        logger.info("testFindByCityId: {}",hotels);
    }



}