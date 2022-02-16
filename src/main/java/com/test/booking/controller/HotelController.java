package com.test.booking.controller;
/*
 * @created 1/28/2022 - 1:34 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.test.booking.exception.HotelNotFoundException;
import com.test.booking.model.Hotel;
import com.test.booking.repo.HotelRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Example;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/hotels")
public class HotelController {

    @Autowired
    HotelRepository hotelRepository;

    @GetMapping()
    List<Hotel> all(Hotel hotel){
//        return hotelRepository.findAll();
        return hotelRepository.findAll(Example.of(hotel)
                , Sort.by(Sort.Direction.ASC,"id"));
    }

    @GetMapping("/{id}")
    Hotel one(@PathVariable Integer id){
        return hotelRepository.findById(id)
                .orElseThrow(()-> new HotelNotFoundException(id));
    }

    @PostMapping()
    Hotel newHotel(@RequestBody Hotel hotel){
        return hotelRepository.save(hotel);
    }

    @PutMapping("/{id}")
    Hotel update(@RequestBody Hotel newHotel,@PathVariable Integer id){
        return hotelRepository.findById(id)
                .map(hotel -> {
                    hotel.setName(newHotel.getName());
                    hotel.setRate(newHotel.getRate());
                    hotel.setCity(newHotel.getCity());
                    return hotelRepository.save(hotel);
                })
                .orElseGet(()-> {
                    newHotel.setHotelId(id);
                    return hotelRepository.save(newHotel);
                });
    }

    @DeleteMapping("/{id}")
    void delete(@PathVariable Integer id){
        hotelRepository.deleteById(id);
    }

}
