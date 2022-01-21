package com.test.lambda;
/*
 * @created 1/21/2022 - 8:10 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 *
 * @see https://www.netjstech.com/2017/08/java-lambda-expressions-interview-questions.html
 *
 * {@docRoot}
 * {@code List}
 * {@link Collections#synchronizedList Collections.synchronizedList}
 * {@link #iterator() iterator}
 * {@link ListIterator#remove() remove}
 * @since 1.0
 *
 * @serial
 *
 * @param
 * @throws IllegalArgumentException if the specified initial capacity
 * @return the number of elements in this list
 */

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.*;
import java.util.function.Predicate;

public class LambdaExpression {
    Logger logger = LoggerFactory.getLogger(LambdaExpression.class);

    /**
     * https://www.netjstech.com/2015/06/lambda-expression-examples-in-java-8.html
     */
    @Test
    public void  simple1(){
        Integer i;
//        System.out.println(()->5);
//        i = () -> 10;
    }

    /**
     * Comparator as Lambda expression example
     * ref https://www.netjstech.com/2015/06/lambda-expression-examples-in-java-8.html
     */

    @Test
    void runnable(){
        new Thread(()-> System.out.println("Runnable Lambda")).start();
    }

    @Test
    void sort(){
        List<String> list=Arrays.asList("Test","Mohammad","Ali");
        logger.info("before ordering:{}",list);
        Collections.sort(list,(String a,String b)->a.compareTo(b));
        logger.info("after ordering:{}",list);
    }

    @Test
    void print(){
        List<String> list=Arrays.asList("Test","Mohammad","Ali");
        list.forEach((st)-> System.out.println(String.format("<<%s>>",st)));
    }

    @Test
    void functionalInterface(){
        List<Person> persons = new ArrayList<Person>();
        IPerson iPerson = Person::new;
        persons.add( iPerson.create("Mohammad","Ramezani",5,'M') );
        persons.add( iPerson.create("Ali","Ramezani",5,'M') );
        persons.add( iPerson.create("Narges","Haghighat",39,'F') );
        persons.add( iPerson.create("Adel","Ramezani",45,'M') );

        persons.forEach((p)->logger.info("person: {}",p));
    }
    
    @Test
    void predicator(){
        List<Person> persons = new ArrayList<Person>();
        persons.add( new Person("Mohammad","Ramezani",5,'M') );
        persons.add( new Person("Ali","Ramezani",5,'M') );
        persons.add( new Person("Narges","Haghighat",39,'F') );
        persons.add( new Person("Adel","Ramezani",45,'M') );

        Predicate<Person> allChildren = p -> p.getAge()<10;
        Predicate<Person> allFemales = p -> p.getGender()=='F';

        List<Person> children = new ArrayList<Person>();
        persons.forEach(p-> {if(allChildren.test(p))children.add(p); } );
        logger.info("children: {}",children);

        List<Person> females = new ArrayList<Person>();
        persons.forEach(p-> {if(allFemales.test(p))females.add(p); } );
        logger.info("females: {}",females);
    }
}


/********
 * person
 */
class Person{
    private String firstName;
    private String lastName;
    private int age;
    private char gender;

    public Person() {
    }

    public Person(String firstName, String lastName, int age, char gender) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.gender = gender;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public char getGender() {
        return gender;
    }

    public void setGender(char gender) {
        this.gender = gender;
    }

    @Override
    public String toString() {
        return "Person{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", age=" + age +
                ", gender=" + gender +
                '}';
    }
}



/********
 * functionalInterface prerequisit
 */
@FunctionalInterface
interface IPerson {
    Person create(String firstName, String lastName, int age, char gender);
}



/******
 * predicator prerequisits
 */