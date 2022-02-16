package com.test.booking.config;
/*
 * @created 1/26/2022 - 11:31 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.zaxxer.hikari.HikariDataSource;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jdbc.repository.config.EnableJdbcRepositories;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseBuilder;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseType;

import javax.sql.DataSource;

@Configuration
@ComponentScan("com.test.booking")
@EnableJdbcRepositories
public class BookingConfiguration {

//    @Bean
//    public DataSource dataSource(){
//        return new EmbeddedDatabaseBuilder()
//                .setType(EmbeddedDatabaseType.H2)
////                .addDefaultScripts()
//                .build();
//    }

    @Bean
    @ConfigurationProperties("app.datasource")
    public DataSource dataSource(){
        return (HikariDataSource) DataSourceBuilder.create()
                .type(HikariDataSource.class).build()
                ;
    }
}
