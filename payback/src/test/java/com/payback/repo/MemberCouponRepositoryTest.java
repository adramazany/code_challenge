package com.payback.repo;

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
class MemberCouponRepositoryTest {

    @Autowired
    MemberCouponRepository memberCouponRepository;

    @Test
    void findByMemberId() {
        List<MemberCoupon> memberCoupons = memberCouponRepository.findByMemberId("1");
//        System.out.println(new Gson().toJson(memberCoupons));
        assertEquals(memberCoupons.size(),2);
    }
}