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

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BinaryOperator;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.IntFunction;
import java.util.stream.Collectors;


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
        Rating john=new Rating();
        john.add(new Review(5, ""));
        john.add(new Review(3, "not bad"));
        double john_rating = john.reviews
                .stream()
                .map(Review::getPoints)
                .reduce(0,Integer::sum)
                / john.reviews.size();
        logger.info("john rating is {} for reviews : {}",john_rating,john.reviews);

        Rating julie = new Rating();
        john.add(new Review(4, "great!"));
        john.add(new Review(2, "terrible experience"));
        john.add(new Review(4, ""));
        double julie_rating = john.computeRating();
        logger.info("julie rating is {} for reviews : {}",julie_rating,julie.reviews);


    }

    /*********************************************************
     *
     collect() can only work with mutable result objects.
     reduce() is designed to work with immutable result objects.
     */

    @Test
    void filter_collect_mutable(){
        List<Integer> numbers = Arrays.asList(1,2,3,4,5,6);

//        Collectors.
        List<Integer> gt_3 = numbers.stream().filter(n->n>3).collect(Collectors.toList());
        logger.info("gt_3 is {}",gt_3);
    }

}


/***********************************************
 * complex custom objects
 *
 */

class Review {

    private int points;
    private String review;

    public Review() {}
    public Review(int points, String review) {
        this.points = points;
        this.review = review;
    }

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }

    public String getReview() {
        return review;
    }

    public void setReview(String review) {
        this.review = review;
    }

    @Override
    public String toString() {
        return "Review{" +
                "points=" + points +
                ", review='" + review + '\'' +
                '}';
    }
}

class Rating {
    double points;
    List<Review> reviews = new ArrayList<Review>();

    public void add(Review review){
        reviews.add(review);
        computeRating();
    }

    double computeRating() {
        double totalPoints = reviews
                .stream()
                .map(Review::getPoints)
                .reduce(0,Integer::sum);
        this.points = totalPoints / reviews.size();
        return this.points;
    }

    public static Rating average(Rating r1,Rating r2){
        Rating combined = new Rating();
        combined.reviews = new ArrayList<>(r1.reviews);
        combined.reviews.addAll(r2.reviews);
        combined.computeRating();
        return combined;
    }


}