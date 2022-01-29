package com.test.lambda;
/*
 * @created 1/24/2022 - 8:25 AM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 *
 * @see https://mkyong.com/java8/java-8-flatmap-example/
 */

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.Stream;

/**
 * Review the below structure. It consists of a 2 levels Stream or a 2d arrays.
 * # Stream<String[]>
 * # Stream<Stream<String>>
 * # String[][]
 *
 * [
 *   [1, 2],
 *   [3, 4],
 *   [5, 6]
 * ]
 * In Java 8, we can use the flatMap to convert the above 2 levels Stream into one Stream level or a 2d array into a 1d array.
 * # Stream<String>
 * # String[]
 *
 * [1, 2, 3, 4, 5, 6]
 *
 *
 *
 *
 */

public class FlatmapTest {
    Logger logger = LoggerFactory.getLogger(FlatmapTest.class);

    @Test
    void array2Stream(){
        String[][] array = new String[][]{{"a", "b"}, {"c", "d"}, {"e", "f"}};
        logger.debug("array={} ...", array);
        // array to a stream
        Stream<String[]> stream1 = Arrays.stream(array);
        System.out.println("Arrays.stream:");
        stream1.forEach(x-> System.out.println( Arrays.toString(x) ));

        // same result
        Stream<String[]> stream2 = Stream.of(array);
        System.out.println("Stream.of:");
        stream1.forEach(x-> System.out.println( Arrays.toString(x) ));
    }


    @Test
    void filter_array(){
        String[][] array = new String[][]{{"a", "b"}, {"c", "d"}, {"e", "f"}};

        // array to a stream
        Stream<String[]> stream1 = Arrays.stream(array);

        // x is a String[]
        List<String[]> result = stream1
                .filter(x -> {
                    for(String s : x){      // really?
                        if(s.equals("a")){
                            return false;
                        }
                    }
                    return true;
                }).collect(Collectors.toList());

        // print array
        result.forEach(x -> System.out.println(Arrays.toString(x)));
    }

    @Test
    void first_flatMap(){
        String[][] array = new String[][]{{"a", "b"}, {"c", "d"}, {"e", "f"}};

        // Java 8
        String[] result = Stream.of(array)  // Stream<String[]>
                .flatMap(Stream::of)        // Stream<String>
                .toArray(String[]::new);    // [a, b, c, d, e, f]

        for (String s : result) {
            System.out.println(s);
        }
    }

    @Test
    void filter_flatted(){

        String[][] array = new String[][]{{"a", "b"}, {"c", "d"}, {"e", "f"}};

        List<String> collect = Stream.of(array)     // Stream<String[]>
                .flatMap(Stream::of)                // Stream<String>
                .filter(x -> !"a".equals(x))        // filter out the a
                .collect(Collectors.toList());      // return a List

        collect.forEach(System.out::println);
    }

    /**
     * I want to point out that dealing with more than one level of Stream is challenging, confusing, and error-prone, and we can use this Stream#flatMap to flatten the 2 levels Stream into one level Stream.
     *
     *
     * Stream<String[]>      -> flatMap ->	Stream<String>
     * Stream<Set<String>>   -> flatMap ->	Stream<String>
     * Stream<List<String>>  -> flatMap ->	Stream<String>
     * Stream<List<Object>>  -> flatMap ->	Stream<Object>
     */

    @Test
    void find_all_books(){
        Developer o1 = new Developer();
        o1.setName("mkyong");
        o1.addBook("Java 8 in Action");
        o1.addBook("Spring Boot in Action");
        o1.addBook("Effective Java (3nd Edition)");

        Developer o2 = new Developer();
        o2.setName("zilap");
        o2.addBook("Learning Python, 5th Edition");
        o2.addBook("Effective Java (3nd Edition)");

        List<Developer> list = new ArrayList<>();
        list.add(o1);
        list.add(o2);

        // hmm....Set of Set...how to process?
        /*Set<Set<String>> collect = list.stream()
                .map(x -> x.getBook())
                .collect(Collectors.toSet());*/

        Set<String> collect =
                list.stream()
                        .map(x -> x.getBook())                              //  Stream<Set<String>>
                        .flatMap(x -> x.stream())                           //  Stream<String>
                        .filter(x -> !x.toLowerCase().contains("python"))   //  filter python book
                        .collect(Collectors.toSet());                       //  remove duplicated

        collect.forEach(System.out::println);

        //or

        Set<String> collect2 = list.stream()
                //.map(x -> x.getBook())
                .flatMap(x -> x.getBook().stream())                 //  Stream<String>
                .filter(x -> !x.toLowerCase().contains("python"))   //  filter python book
                .collect(Collectors.toSet());
        collect2.forEach(System.out::println);
    }

    @Test
    void order_and_LineItems(){
        LineItem item1 = new LineItem(1, "apple", 1, new BigDecimal("1.20"), new BigDecimal("1.20"));
        LineItem item2 = new LineItem(2, "orange", 2, new BigDecimal(".50"), new BigDecimal("1.00"));
        Order order1 = new Order(1, "A0000001", Arrays.asList(item1, item2), new BigDecimal("2.20"));

        LineItem item3 = new LineItem(3, "monitor BenQ", 5, new BigDecimal("99.00"), new BigDecimal("495.00"));
        LineItem item4 = new LineItem(4, "monitor LG", 10, new BigDecimal("120.00"), new BigDecimal("1200.00"));
        Order order2 = new Order(2, "A0000002", Arrays.asList(item3, item4), new BigDecimal("1695.00"));

        LineItem item5 = new LineItem(5, "One Plus 8T", 3, new BigDecimal("499.00"), new BigDecimal("1497.00"));
        Order order3 = new Order(3, "A0000003", Arrays.asList(item5), new BigDecimal("1497.00"));
        List<Order> orders = Arrays.asList(order1, order2, order3);

        /*
            Stream<List<LineItem>> listStream = orders.stream()
                    .map(order -> order.getLineItems());

            Stream<LineItem> lineItemStream = orders.stream()
                    .flatMap(order -> order.getLineItems().stream());
        */

        // sum the line items' total amount
        BigDecimal sumOfLineItems = orders.stream()
                .flatMap(order -> order.getLineItems().stream())    //  Stream<LineItem>
                .map(line -> line.getTotal())                       //  Stream<BigDecimal>
                .reduce(BigDecimal.ZERO, BigDecimal::add);          //  reduce to sum all

        // sum the order's total amount
        BigDecimal sumOfOrder = orders.stream()
                .map(order -> order.getTotal())                     //  Stream<BigDecimal>
                .reduce(BigDecimal.ZERO, BigDecimal::add);          //  reduce to sum all

        System.out.println(sumOfLineItems);                         // 3194.20
        System.out.println(sumOfOrder);                             // 3194.20

        if (!sumOfOrder.equals(sumOfLineItems)) {
            System.out.println("The sumOfOrder is not equals to sumOfLineItems!");
        }
    }

    @Test
    void Splits_the_line_by_spaces()throws IOException {
        Path path = Paths.get("C:\\test\\test.txt");

        // read file into a stream of lines
        Stream<String> lines = Files.lines(path, StandardCharsets.UTF_8);

        // stream of array...hard to process.
        // Stream<String[]> words = lines.map(line -> line.split(" +"));

        // stream of stream of string....hmm...better flat to one level.
        // Stream<Stream<String>> words = lines.map(line -> Stream.of(line.split(" +")));

        // result a stream of words, good!
        Stream<String> words = lines.flatMap(line -> Stream.of(line.split(" +")));

        // count the number of words.
        long noOfWords = words.count();

        System.out.println(noOfWords);  // 16
    }

    @Test
    void flatMap_and_primitive_type(){
        int[] array = {1, 2, 3, 4, 5, 6};

        //Stream<int[]>
        Stream<int[]> streamArray = Stream.of(array);

        //Stream<int[]> -> flatMap -> IntStream
        IntStream intStream = streamArray.flatMapToInt(x -> Arrays.stream(x));

        intStream.forEach(x -> System.out.println(x));

        //long

        long[] array2 = {1, 2, 3, 4, 5, 6};

        Stream<long[]> longArray = Stream.of(array2);

        LongStream longStream = longArray.flatMapToLong(x -> Arrays.stream(x));

        System.out.println(longStream.count());


    }

}


/*************************************************************************
 *
 */
class Developer {

    private Integer id;
    private String name;
    private Set<String> book;

    //getters, setters, toString

    public void addBook(String book) {
        if (this.book == null) {
            this.book = new HashSet<>();
        }
        this.book.add(book);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Set<String> getBook() {
        return book;
    }
}


class Order {

    private Integer id;
    private String invoice;
    private List<LineItem> lineItems;
    private BigDecimal total;

    public Order(Integer id, String invoice, List<LineItem> lineItems, BigDecimal total) {
        this.id = id;
        this.invoice = invoice;
        this.lineItems = lineItems;
        this.total = total;
    }

    public List<LineItem> getLineItems() {
        return lineItems;
    }

    public BigDecimal getTotal() {
        return total;
    }

    // getter, setters, constructor
}

class LineItem {

    private Integer id;
    private String item;
    private Integer qty;
    private BigDecimal price;
    private BigDecimal total;

    public LineItem(Integer id, String item, Integer qty, BigDecimal price, BigDecimal total) {
        this.id = id;
        this.item = item;
        this.qty = qty;
        this.price = price;
        this.total = total;
    }

    public BigDecimal getTotal() {
        return total;
    }


    // getter, setters, constructor
}
