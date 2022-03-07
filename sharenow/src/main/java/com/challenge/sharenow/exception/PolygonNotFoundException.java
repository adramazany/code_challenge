package com.challenge.sharenow.exception;
/*
 * @created 1/28/2022 - 6:55 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

public class PolygonNotFoundException extends RuntimeException {

    public PolygonNotFoundException(String id) {
        super("Could not find Polygon "+id);
    }
}
