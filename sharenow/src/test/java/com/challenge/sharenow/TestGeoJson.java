package com.challenge.sharenow;
/*
 * @created 3/6/2022 - 7:02 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.challenge.sharenow.model.GeoPolygon;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;

import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import org.geotools.geojson.GeoJSONUtil;
import org.geotools.geojson.geom.GeometryJSON;
//import org.json.simple.JSONObject;
//import org.json.simple.JSONArray;
//import org.json.simple.parser.JSONParser;
//import org.json.simple.parser.ParseException;
import org.junit.jupiter.api.Test;
import org.locationtech.jts.geom.Geometry;
import org.locationtech.jts.geom.GeometryCollection;
import org.locationtech.jts.geom.Point;
import org.locationtech.jts.geom.Polygon;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;

public class TestGeoJson {

    @Test
    void testGeometryJSON() throws IOException {
        double longitude=9.1371735, latitude=48.790337;
        Point point = null;
        GeometryJSON gtjson = new GeometryJSON();
        point = gtjson.readPoint( new StringReader( "{\"type\":\"Point\", \"coordinates\":[" + longitude + ","
                + latitude + "]}" ) );
        System.out.println("TestGeoJson.testGeometryJSON"+point.toString());
//        gtjson.readGeometryCollection("")
    }

    @Test
    void testLoadGeoAsJson() throws IOException {
        String jsonStr = Files.readString(Paths.get("D:\\workspace\\code_challenge\\sharenow\\src\\main\\resources\\polygons.json"));
        Gson gson=new Gson();
        JsonArray jsonAr = gson.fromJson(jsonStr, JsonArray.class);
        System.out.println("jsonAr size="+jsonAr.size());//154

        HashMap<String,Integer> geoTypesCounter = new HashMap<>();
        Iterator<JsonElement> iter =jsonAr.iterator();
        while(iter.hasNext()){
            JsonElement o= iter.next();
            String geoType =  o.getAsJsonObject().get("geometry").getAsJsonObject().get("type").getAsString();
            Integer count = geoTypesCounter.get(geoType);
            if (count == null) count = 0;
            geoTypesCounter.put(geoType, count + 1);
        }
        System.out.println("geoTypesCounter="+geoTypesCounter.toString());
    }

    class GeoInfo{
        String _id;
        String name;
        String cityId;
        String type;
        JsonObject geometry;
        Geometry geometryObj;

        public GeoInfo(){}
        public GeoInfo(String _id, String name, String cityId, String type, JsonObject geometry) {
            this._id = _id;
            this.name = name;
            this.cityId = cityId;
            this.type = type;
            this.geometry = geometry;
        }

        public Geometry getGeometryObj() {
            if(geometryObj==null) {
                try {
                    this.geometryObj = new GeometryJSON().read(geometry.toString());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return geometryObj;
        }

        public void setGeometry(JsonObject geometry) {
            this.geometry = geometry;
        }
    }

    @Test
    void testLoadGeoAsGeometry() throws IOException {
        String jsonStr = Files.readString(Paths.get("D:\\workspace\\code_challenge\\sharenow\\src\\main\\resources\\polygons.json"));
        Gson gson=new Gson();
        GeometryJSON geometryJSON = new GeometryJSON();
        JsonArray jsonAr = gson.fromJson(jsonStr, JsonArray.class);
        System.out.println("jsonAr size="+jsonAr.size());//154

        HashMap<String,GeoInfo> geoTypesCounter = new HashMap<>();
        Iterator<JsonElement> iter =jsonAr.iterator();
        while(iter.hasNext()){
            JsonObject o= iter.next().getAsJsonObject();
            GeoInfo geo = new GeoInfo();
            geo._id = o.get("_id").getAsString();
            geo.name = o.get("name").getAsString();
            geo.cityId = o.get("cityId").getAsString();
            geo.type = o.get("type").getAsString();
            geo.geometryObj = geometryJSON.read(o.get("geometry").toString());
            geoTypesCounter.put(geo._id, geo);
        }
        System.out.println("geoTypesCounter="+geoTypesCounter.toString());
    }

    @Test
    void testFindPointInPolygons() throws IOException {
        String jsonStr = Files.readString(Paths.get("D:\\workspace\\code_challenge\\sharenow\\src\\main\\resources\\polygons.json"));
        Gson gson=new Gson();
        ArrayList<GeoInfo> geometries = gson.fromJson(jsonStr,new TypeToken<ArrayList<GeoInfo>>(){}.getType() );
        System.out.println("Ar size="+geometries.size());//154

        double longitude = 9.32108402253,latitude=48.7508977740;
        Point point = new GeometryJSON().readPoint( new StringReader(
                "{\"type\":\"Point\", \"coordinates\":[" + longitude + ","+ latitude + "]}" ) );

        GeoInfo geoInfo = geometries.stream().filter(g-> {
            Polygon polygon = (Polygon)g.getGeometryObj();
            return polygon!=null && polygon.contains(point);
        }).findFirst().orElseThrow();

        System.out.println("find geometry:"+geoInfo.name);

//        for(GeoInfo geoInfo :geometries.values()){
//            Polygon polygon = (Polygon)geoInfo.geometry;
//            if(polygon.contains(point)){
//                System.out.println("find geometry:"+geoInfo.name);
//                break;
//            }
//        }
//        System.out.println("not found!!!");

    }

    @Test
    void testFindPointInPolygons2() throws IOException {
        String jsonStr = Files.readString(Paths.get("D:\\workspace\\code_challenge\\sharenow\\src\\main\\resources\\polygons.json"));
        ObjectMapper mapper = new ObjectMapper();
        List<GeoPolygon> geometries = mapper.readValue(jsonStr,new TypeReference<List<GeoPolygon>>(){});
        System.out.println("Ar size="+geometries.size());//154

//        double longitude = 9.32108402253,latitude=48.7508977740;
//        Point point = new GeometryJSON().readPoint( new StringReader(
//                "{\"type\":\"Point\", \"coordinates\":[" + longitude + ","+ latitude + "]}" ) );
//
//        GeoInfo geoInfo = geometries.stream().filter(g-> {
//            Polygon polygon = (Polygon)g.getGeometryObj();
//            return polygon!=null && polygon.contains(point);
//        }).findFirst().orElseThrow();
//
//        System.out.println("find geometry:"+geoInfo.name);
    }

}
