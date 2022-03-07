package com.challenge.sharenow.util;
/*
 * @created 3/7/2022 - 12:49 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.challenge.sharenow.model.GeoPolygon;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import org.geotools.geojson.geom.GeometryJSON;
import org.locationtech.jts.geom.Geometry;
import org.locationtech.jts.geom.Point;
import org.springframework.core.io.DefaultResourceLoader;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.StringReader;
import java.util.ArrayList;

public class GeoUtil {

    private static GeometryJSON geometryJSON=new GeometryJSON();

    public static Point createPoint(double longitude,double latitude) throws IOException {
        Point point = geometryJSON.readPoint( new StringReader(
                "{\"type\":\"Point\", \"coordinates\":[" + longitude + ","+ latitude + "]}" ) );
        return point;
    }

    public static Geometry read(Object input) throws IOException {
        return geometryJSON.read(input);
    }



}
