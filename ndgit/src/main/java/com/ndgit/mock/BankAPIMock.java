package com.ndgit.mock;

import java.util.Random;
import java.util.UUID;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

import com.github.tomakehurst.wiremock.WireMockServer;
import com.github.tomakehurst.wiremock.common.FileSource;
import com.github.tomakehurst.wiremock.extension.Parameters;
import com.github.tomakehurst.wiremock.extension.ResponseTransformer;
import com.github.tomakehurst.wiremock.http.Request;
import com.github.tomakehurst.wiremock.http.Response;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;

import static com.github.tomakehurst.wiremock.client.WireMock.aResponse;
import static com.github.tomakehurst.wiremock.client.WireMock.get;
import static com.github.tomakehurst.wiremock.client.WireMock.urlMatching;
import static com.github.tomakehurst.wiremock.core.WireMockConfiguration.wireMockConfig;
import static com.github.tomakehurst.wiremock.http.HttpHeader.httpHeader;

/**
 * This WireMock implements an imaginary bank backend API implementing payments retrieval.
 * It is a proprietary legacy system, so no changes possible.
 */
@Slf4j
@Component
public class BankAPIMock {

    private static final Random RANDOMIZER = new Random();

    private final WireMockServer wireMockServer;

    public BankAPIMock(@Value("${bank.api.port}") int port) {
        this.wireMockServer = new WireMockServer(wireMockConfig().port(port).extensions(new BankApiResponseGenerator()));
    }

    @PostConstruct
    public void init() {
        wireMockServer.start();
        wireMockServer.stubFor(get(urlMatching("/payment/(\\d*)"))
                                       .willReturn(aResponse().withUniformRandomDelay(100, 1000)));
    }

    @PreDestroy
    public void finish() {
        wireMockServer.stop();
    }

    private static class BankApiResponseGenerator extends ResponseTransformer {

        private final ExecutorService executor = Executors.newFixedThreadPool(2);

        @Override
        public String getName() {
            return "BankApiResponseGenerator";
        }

        @Override
        public Response transform(Request request, Response response, FileSource files, Parameters parameters) {
            String bankPaymentId = UUID.randomUUID().toString();
            String status = RANDOMIZER.nextBoolean() ? "ACCEPTED" : "REJECTED";

            Future<Response> future = executor.submit(() -> buildResponse(response, bankPaymentId, status));

            try {
                return future.get(4, TimeUnit.SECONDS);
            } catch (Exception e) {
                log.error("Error building response", e);
                return Response.Builder.like(response).but().status(400).build();
            }
        }

        private Response buildResponse(Response response, String bankPaymentId, String status) throws InterruptedException {
            Thread.sleep(RANDOMIZER.nextInt(8000));

            if (RANDOMIZER.nextBoolean()) {
                return Response.Builder.like(response)
                        .but().status(200)
                        .body(String.format("{ \"status\": \"%s\", \"bankPaymentId\": \"%s\" }", status, bankPaymentId))
                        .headers(response.getHeaders().plus(httpHeader("Content-Type", MediaType.APPLICATION_JSON_VALUE)))
                        .build();
            } else {
                return Response.Builder.like(response).but().status(500).build();
            }
        }
    }
}
