package com.challenge.sharenow.configuration;
/*
 * @created 3/7/2022 - 8:14 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.client.RestTemplate;

@Configuration
@EnableScheduling
public class GeoConfiguration {

    @Bean
    RestTemplate restTemplate(){
        return new RestTemplate();
    }

}
