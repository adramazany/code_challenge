package com.challenge.sharenow.repository;
/*
 * @created 3/6/2022 - 11:48 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.challenge.sharenow.model.GeoPolygon;
import com.challenge.sharenow.model.Position;
import com.challenge.sharenow.util.GeoUtil;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import org.geotools.geojson.GeoJSONUtil;
import org.geotools.geojson.geom.GeometryJSON;
import org.locationtech.jts.geom.Point;
import org.locationtech.jts.geom.Polygon;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.io.DefaultResourceLoader;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

@Component
public class PolygonRepository {
    Logger logger = LoggerFactory.getLogger(PolygonRepository.class);

    HashMap<String,GeoPolygon> geoPolygons;

    public HashMap<String,GeoPolygon> getGeoPolygons() {
        if(geoPolygons ==null){
            geoPolygons=new HashMap<>();
            try {
                Reader r=new InputStreamReader(new DefaultResourceLoader().getResource("polygons.json").getInputStream());
                List<GeoPolygon> polygons = new Gson().fromJson(r, new TypeToken<ArrayList<GeoPolygon>>() {}.getType());
                geoPolygons.putAll( polygons.stream().collect(
                        Collectors.toMap(GeoPolygon::get_id, Function.identity(),(existing, replacement)->replacement)));
//                System.out.println("Ar size=" + geoPolygons.size());//154
            }catch(Exception ex){
                ex.printStackTrace();
            }
        }
        return geoPolygons;
    }

    public GeoPolygon findById(String id){
        return getGeoPolygons().get(id);
    }

    public GeoPolygon[] findAll(){
        return getGeoPolygons().values().toArray(GeoPolygon[]::new);
    }

    public GeoPolygon findIdByLngLat(Position position)  {
        try{
            return findByLngLat(position.getLongitude(), position.getLatitude());
        }catch(Exception ex){
//            ex.printStackTrace();
            logger.error("polygon not found at :"+position+" , "+ex.getMessage());
        }
        return null;
    }
    public GeoPolygon findByLngLat(double longitude, double latitude) throws IOException {
        Point point = GeoUtil.createPoint(longitude, latitude);

        return getGeoPolygons().values().stream().filter(g-> {
            Polygon polygon = (Polygon)g.getGeometryObj();
            return polygon!=null && polygon.contains(point);
        }).findFirst().orElseThrow();
    }

}
