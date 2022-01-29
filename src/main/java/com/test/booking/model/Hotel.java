package com.test.booking.model;
/*
 * @created 1/26/2022 - 12:30 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */


import javax.persistence.*;

@Entity
@Table(name="hotel")
@NamedNativeQuery(name = "Hotel.findByCityId"
,query = "select * from HOTEL where CITY_ID=:cityId"
,resultClass = Hotel.class
)

public class Hotel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    Integer hotelId;
    String name;
    Integer rate;
    Integer cityId;

    public Integer getHotelId() {
        return hotelId;
    }

    public void setHotelId(Integer hotelId) {
        this.hotelId = hotelId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getRate() {
        return rate;
    }

    public void setRate(Integer rate) {
        this.rate = rate;
    }

    public Integer getCityId() {
        return cityId;
    }

    public void setCityId(Integer cityId) {
        this.cityId = cityId;
    }

    @Override
    public String toString() {
        return "Hotel{" +
                "hotelId=" + hotelId +
                ", name='" + name + '\'' +
                ", rate=" + rate +
                ", cityId=" + cityId +
                '}';
    }
}
