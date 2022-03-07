package com.challenge.sharenow.model;
/*
 * @created 3/6/2022 - 11:41 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 *
 * It contains limited data that we need,
 * Then we could extends the properties by requirements
 */

import com.challenge.sharenow.util.GeoUtil;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.google.gson.JsonObject;
import org.locationtech.jts.geom.Geometry;

import java.io.IOException;
import java.util.HashSet;

public class GeoPolygon {
    String _id;
    String name;
    String cityId;
    String type;
    JsonObject geometry;//JsonObject
    Geometry geometryObj;
    HashSet<String> vins = new HashSet<>();

    public GeoPolygon() {}

    public GeoPolygon(String _id, String name, String cityId, String type, JsonObject geometry) {
        this._id = _id;
        this.name = name;
        this.cityId = cityId;
        this.type = type;
        this.geometry = geometry;
    }

    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCityId() {
        return cityId;
    }

    public void setCityId(String cityId) {
        this.cityId = cityId;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    @JsonIgnore
    public JsonObject getGeometry() {
        return geometry;
    }

    public void setGeometry(JsonObject geometry) {
        this.geometry = geometry;
    }

    public void setGeometryObj(Geometry geometryObj) {
        this.geometryObj = geometryObj;
    }

    @JsonIgnore
    public Geometry getGeometryObj() {
        if(geometryObj==null) {
            try {
                this.geometryObj = GeoUtil.read(geometry.toString());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return geometryObj;
    }

    public HashSet<String> getVins() {
        return vins;
    }

    public boolean addVin(String s) {
        return vins.add(s);
    }

    public boolean removeVin(String o) {
        return vins.remove(o);
    }


}
