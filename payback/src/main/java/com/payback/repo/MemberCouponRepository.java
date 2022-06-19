package com.payback.repo;
/*
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.payback.model.MemberCoupon;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MemberCouponRepository extends JpaRepository<MemberCoupon,Integer> {

    @Query(nativeQuery = true,name = "MemberCoupon.findByMemberId",value = "SELECT * FROM member_coupon t " +
            " WHERE t.member_id=:memberId and trunc(sysdate) between valid_from and valid_until " +
            " order by valid_until DESC ")
    List<MemberCoupon> findByMemberId(@Param("memberId") String memberId);

}
