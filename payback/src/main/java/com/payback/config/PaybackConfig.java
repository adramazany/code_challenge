package com.payback.config;
import com.zaxxer.hikari.HikariDataSource;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jdbc.repository.config.EnableJdbcRepositories;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

import javax.sql.DataSource;
/*
 * @created 6/16/2022 - 4:56 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

@Configuration
@EnableJdbcRepositories
@EnableSwagger2
public class PaybackConfig {

/*
    @Bean
    @ConfigurationProperties("app.datasource")
    public DataSource dataSource(){
        return (HikariDataSource) DataSourceBuilder.create()
                .type(HikariDataSource.class).build()
                ;
    }
*/

    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
//                .apis(RequestHandlerSelectors.any())
                .apis(RequestHandlerSelectors.basePackage("com.payback"))
                .paths(PathSelectors.any())
                .build();
    }

}
