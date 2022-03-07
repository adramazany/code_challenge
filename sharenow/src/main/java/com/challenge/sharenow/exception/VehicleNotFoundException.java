package com.challenge.sharenow.exception;
/*
 * @created 1/28/2022 - 6:55 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

public class VehicleNotFoundException extends RuntimeException {

    public VehicleNotFoundException(String vin) {
        super("Could not find Vehicle "+vin);
    }
}
