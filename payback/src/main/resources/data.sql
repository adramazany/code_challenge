insert into coupon (coupon_Id,coupon_Name,discount_Amount,discount_Type,expiration_Date)
values ('1','Spring Discount',2,'Fix Amount',PARSEDATETIME('2022-06-21','yyyy-MM-dd'));
insert into coupon (coupon_Id,coupon_Name,discount_Amount,discount_Type,expiration_Date)
values ('2','Weekend Discount',1,'Fix Amount',PARSEDATETIME('2022-12-30','yyyy-MM-dd'));

insert into member_coupon (member_Id,coupon_Id,valid_From,valid_Until,latitude,longitude)
values ( '1', '1', sysdate, sysdate ,34.052234,-118.243685);-- los angles
insert into member_coupon (member_Id,coupon_Id,valid_From,valid_Until,latitude,longitude)
values ( '1', '2', PARSEDATETIME('2022-01-01','yyyy-MM-dd'), PARSEDATETIME('2022-07-30','yyyy-MM-dd') ,38.581572,-121.4944);-- scramento
