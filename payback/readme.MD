# Coding challenge
Your task is to implement a web service, which exposes this "GetMemberCoupons" REST endpoint. To return a given member's coupons, the web
service must query the database table (see description above) for the member's assigned coupons. You are free to choose whatever technology
you like for the web service and the database (relational or NoSQL).

## Requirements:
* You don't need to spend more than a few hours on your implementation. A basic running version (with one or two unit tests) is
absolutely enough
  - you could run the code by PaybackApplication class (a very basic running version)
  - a few unit test are located in MemberCouponRepositoryTest and MemberCouponServiceTest just one method of main classes
  - it could be located and tested in http://localhost:8080/swagger-ui.html link
* Only return coupons for the memberId, which is specified as a parameter in the REST call
  - link http://localhost:8080/swagger-ui.html#/member-coupon-controller/getMemberCouponsUsingGET is for getting data
* Only return coupons which are currently valid (i.e. the current date is between the validFrom and validUntil date)
  - just 2 records initialized in data.sql for MemberCoupouns by different dates 
* Sort the list of returned coupons by the validUntil date in descending order
  - the result filtered and sorted by query in repository
* Keep performance and scalability in mind
  - JPA used in this code challenge to enable casjing of multiple requested members coupons
  - java streaming used in processing of distance between current location and target locations to increase performance
  - docker file attached to enable distribution and creating multiple instance in containers like kubernetes
  - helper files to build and run docker already prepared  
    
* When you are finished, please push your code to a git repository and give us access
    - done

## Additional requirement:
* Each coupon is associated to a specified partner Branch location (e.g. Supermarket A in City B) represented by the latitude and
longitude coordinates.
  - done
o Add 2 columns to the coupon table to store the latitude and longitude information for each coupon
* Extend the parameters passed to the GetMemberCoupons Service to also include the current location of the member (in latitude and
longitude)
  - done
* The GetMemberCoupons Service should now return a coupon list that is sorted by distance (nearest first).
  - it is done in validUntil class by calculating distance between current location and coupons location
  - it is prepared in another REST already named GetMemberCoupons by extra parameters

## Notes
To keep it simple:
* Inserting data into the "assigned coupons" table can be done via script (e.g. shell, sql, ...). No need to implement a REST Endpoint for
doing so.
* Implementing a frontend is out of scope. Calling the " GetMemberCoupons" endpoint via curl or the browser is sufficient.