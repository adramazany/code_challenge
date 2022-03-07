package com.challenge.sharenow.model;
/*
 * @created 3/7/2022 - 8:06 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */


public class Vehicle {
    Integer id;
    Integer locationId;
    String vin;
    String numberPlate;
    Position position;
    Double fuel;
    String model;
    String polygonId;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getLocationId() {
        return locationId;
    }

    public void setLocationId(Integer locationId) {
        this.locationId = locationId;
    }

    public String getVin() {
        return vin;
    }

    public void setVin(String vin) {
        this.vin = vin;
    }

    public String getNumberPlate() {
        return numberPlate;
    }

    public void setNumberPlate(String numberPlate) {
        this.numberPlate = numberPlate;
    }

    public Position getPosition() {
        return position;
    }

    public void setPosition(Position position) {
        this.position = position;
    }

    public Double getFuel() {
        return fuel;
    }

    public void setFuel(Double fuel) {
        this.fuel = fuel;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getPolygonId() {
        return polygonId;
    }

    public void setPolygonId(String polygonId) {
        this.polygonId = polygonId;
    }
}
