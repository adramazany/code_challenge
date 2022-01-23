package com.test.lambda;
/*
 * @created 1/23/2022 - 9:04 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 *
 * The Key Concepts: Identity, Accumulator and Combiner
 */

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Arrays;
import java.util.List;
import java.util.function.BinaryOperator;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.IntFunction;


import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

public class StreamTest {
    Logger logger = LoggerFactory.getLogger(StreamTest.class);

    @Test
    void identity_accumulator(){
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
        int identity=0;
        BinaryOperator<Integer> accumulator_lambda = (subtotal, element) -> subtotal + element;
        int result = numbers
                .stream()
                .reduce(identity, accumulator_lambda);
        assertThat(result).isEqualTo(21);

        logger.info("identity_accumulator: total of {} is {}",numbers,result);
    }

    @Test
    void accumulator_method_refrence(){
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
        BinaryOperator<Integer> accumulator_method_ref = Integer::sum;

        int result = numbers.stream().reduce(0,accumulator_method_ref);
        assertThat(result).isEqualTo(21);

        logger.info("accumulator_method_refrence : total of {} is {}",numbers,result);
    }

    @Test
    void parallelStream_combiner(){
        List<String> letters = Arrays.asList("a","B","c","D","e");
        BinaryOperator<String> accumulator = (partialStr,element) -> partialStr+element.toUpperCase();
        BinaryOperator<String> combiner = String::concat;

        String result = letters.parallelStream().reduce("",accumulator,combiner);
        assertThat(result).isEqualTo("ABCDE");
        logger.info("parallelStream_combiner: combination of {} is {}",letters,result);
    }

    @Test
    void lambda_try_catch(){
        List<Integer> numbers = Arrays.asList(1,2,3,4,5,6);
        int divider=2;
        BinaryOperator<Integer> accumulator = (sub,element) -> {
            try{
                return sub/divider + element/divider;
            }catch(ArithmeticException e){
                logger.error("error in dividing:",e);
            }
            return 0;
        };

        int result = numbers.stream().reduce(0,accumulator);
        logger.info("dividing numbers {} to {} is {}",numbers,divider,result);
    }

    @Test
    void map_reduce_objects(){

    }

}


/***********************************************
 * complex custom objects
 *
 */