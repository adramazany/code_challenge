package com.test.booking.exception;
/*
 * @created 1/28/2022 - 6:55 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

public class HotelNotFoundException extends RuntimeException {

    public HotelNotFoundException(Integer hotelId) {
        super("Could not find hotel "+hotelId);
    }
}
