package com.payback.repo;
/*
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.payback.model.Coupon;
import com.payback.model.MemberCoupon;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CouponRepository extends JpaRepository<Coupon,String> {

}
