package com.challenge.sharenow.configuration;
/*
 * @created 3/7/2022 - 8:14 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class GeoConfiguration {

    @Bean
    RestTemplate restTemplate(){
        return new RestTemplate();
    }
}
