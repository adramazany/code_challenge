package com.payback.service;

import com.google.gson.Gson;
import com.payback.model.MemberCoupon;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/*
 * @author adel.ramezani (adramazany@gmail.com)
 */

@SpringBootTest
class MemberCouponServiceTest {

    @Autowired
    MemberCouponService memberCouponService;

    @Test
    void getMemberCouponsNearestFirst() {
        //long beach = lat : 33.77005 , long -118.193739  -- near to los-angles
        List<MemberCoupon> memberCoupons = memberCouponService.getMemberCouponsNearestFirst("1",33.77005 , -118.193739);
        System.out.println(new Gson().toJson(memberCoupons));
        assertEquals(memberCoupons.get(0).getCoupon().getCouponId(),"1");


    }
}