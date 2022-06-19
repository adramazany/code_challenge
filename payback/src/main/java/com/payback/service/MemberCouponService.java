package com.payback.service;
/*
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.payback.model.MemberCoupon;
import com.payback.repo.MemberCouponRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Comparator;
import java.util.List;

@Service
public class MemberCouponService {

    @Autowired
    MemberCouponRepository memberCouponRepository;

    public List<MemberCoupon> getMemberCoupons(String memberId){
        return memberCouponRepository.findByMemberId(memberId);
    }

    public List<MemberCoupon> getMemberCouponsNearestFirst(String memberId,Double latitude,Double longitude){
        List<MemberCoupon> list = memberCouponRepository.findByMemberId(memberId);

        Comparator<MemberCoupon> comparator
                = (c1, c2) ->  Double.compare( distance(latitude,longitude,c1.getLatitude(),c1.getLongitude())
                                                ,distance(latitude,longitude,c2.getLatitude(),c2.getLongitude()));

        list.sort(comparator);

        return list;
    }

    double distance(double lat1, double lon1, double lat2, double lon2) {
        if ((lat1 == lat2) && (lon1 == lon2)) {
            return 0;
        }
        else {
            double theta = lon1 - lon2;
            double dist = Math.sin(Math.toRadians(lat1)) * Math.sin(Math.toRadians(lat2)) + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2)) * Math.cos(Math.toRadians(theta));
            dist = Math.acos(dist);
            dist = Math.toDegrees(dist);
            dist = dist * 60 * 1.1515;
            dist = dist * 1.609344;//Kilometers
            return (dist);
        }
    }

}
