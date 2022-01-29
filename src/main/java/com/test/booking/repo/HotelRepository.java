package com.test.booking.repo;
/*
 * @created 1/26/2022 - 12:35 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.test.booking.model.Hotel;
//import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
//public interface HotelRepository extends CrudRepository<Hotel,Integer> {
public interface HotelRepository extends JpaRepository<Hotel,Integer> {

    default <S extends Hotel> S update(S entity) {
        if(entity.getHotelId()==null)throw new RuntimeException("id required!");
        return save(entity);
    }

//    @Query(name = "Hotel.findByCityId")
    @Query(nativeQuery = true,name = "Hotel.findByCityId")
    List<Hotel> findByCityId(@Param("cityId") Integer cityId);



}
