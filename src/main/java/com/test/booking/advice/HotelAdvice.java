package com.test.booking.advice;
/*
 * @created 1/28/2022 - 7:46 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.test.booking.exception.HotelNotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

@ControllerAdvice
public class HotelAdvice {

    @ResponseBody
    @ExceptionHandler(HotelNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    String hotelNotFoundHandler(HotelNotFoundException ex){
        return ex.getMessage();
    }

/*
    @ResponseBody
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    String exceptionHandler(Exception ex){
        return "General failure: "+ex.getMessage();
    }
*/
}
