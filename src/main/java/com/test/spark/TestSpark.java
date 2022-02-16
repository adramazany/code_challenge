package com.test.spark;
/*
 * @created 2/8/2022 - 6:33 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.junit.jupiter.api.Test;

public class TestSpark {



    @Test
    void testSparkSession(){
        System.out.println("testSparkSession");
        SparkSession spark = SparkSession
                .builder()
                .appName("test spark")
                .config("spark.master", "local") /* SparkException: A master URL must be set in your configuration */
                .config("spark.some.config.option","some-value")
                .getOrCreate();
        System.out.println("spark version="+spark.version());
    }

    @Test
    void testCreatingDataframe(){
//        Dataset<Row> df = spark().read().json("datalake/searches/");
        Dataset<Row> df = spark().read().json("D:/workspace/code_challenge/src/main/resources/datalake/test.json");
        df.show();
    }


    SparkSession spark(){
        return SparkSession
                .builder()
                .appName("test spark")
                .config("spark.master","local")
                .getOrCreate();
    }


}
