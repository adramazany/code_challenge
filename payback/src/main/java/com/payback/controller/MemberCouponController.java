package com.payback.controller;
/*
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.payback.model.MemberCoupon;
import com.payback.service.MemberCouponService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/GetMemberCoupons")
public class MemberCouponController {

    @Autowired
    MemberCouponService memberCouponService;

    @GetMapping("/{memberId}")
    List<MemberCoupon> getMemberCoupons(String memberId){
        return memberCouponService.getMemberCoupons(memberId);
    }

    @GetMapping("/{memberId}/{latitude}/{longitude}")
    List<MemberCoupon> getMemberCouponsNearestFirst(String memberId,Double latitude,Double longitude){
        return memberCouponService.getMemberCouponsNearestFirst(memberId,latitude,longitude);
    }

}
