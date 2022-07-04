# ndgit Java challenge
This coding challenge is designed to test your problem-solving skills on some close-to-real example.
You have to implement a Payments Synchronisation Microservice that persists payment information in its own database 
and periodically requests updates from the bank backend system. 

As in the real world, the bank backend is slow and unstable - this behavior is simulated by `BankAPIMock` class.

## Application features and requirements

1. Adding a new Payment to the database;
   - done
2. Updating Payment status;
   - done
3. Periodically request Payment updates from the Bank backend to populate bankPaymentId field for the records that do not have one yet;
   - done
4. Payment status can be retrieved from the bank backend only in case it has not yet been set by the microservice;
   - done
5. In production this microservice will work under high load. Database will contain millions of records and multiple instances of the service will run in parallel;
   - The strategies that used are very good when we are using multiple parallel instance in production, and we don't want to use MQ.
6. Around 500.000 new payments are expected to be stored in the system per month;
   - By this strategy the performance is depends on tuning database and adding instance of microservice. 
7. Each Payment should receive a bankPaymentId in no longer than 1 week after it is added to the system;
   - Every instance try to accomplish all empty payment status in every try until encountered exception from calling bank API, so wait until next try

## Tasks

1. Implement the missing parts of the application;
   - adding PaymentRepository extends JpaRepository (because we needed findAllById)
     and implementing a native query method Payment.findNextEmptyBankPaymentId (native selected just for simplicity reason, It is complex in JPQL and JPQL has not "limit" syntax and also it could be implemented by Matcher for finding null values)
     **and This method had main role when multiple instance of microservice running simultaneously.**
   - implementing updateStatus and addPayment of PaymentServiceImpl by using PaymentRepository
     and updateBankResponse method to the service for updating payments by bank result
   - implementing BankClientApiImpl for BankClientApi interface
     adding bank.api.url property in the application.yml and BankClientApiImpl to enabling change of bank target api in production platform
     define RestTemplate bean in the JavaChallengeApplication by using RestTemplateBuilder for calling banking APIs
     **adding bank.api.connectTimeout and bank.api.readTimeout properties in the application.yml and set them at RestTemplate bean to enable optimizing banking API call in production**
   - implementing PeriodicallyRequestBank service by PeriodicallyRequestBankImpl for Periodically request Payment updates from the Bank backend
     implemnting scheduleBankRequest method by :
        - getting just one EmptyBankPaymentId
        - change the status of fetched record to IN-PROGRESS immediately
        - calling bank API 
        - update payment by bank paymentId and status
        - or reverse payment status to previous status if API call failed and break the loop
        - repeat until all payments processed or one exception occured
     **above flow is the best flow when we have multiple instance of microservice that wants to process payments**
     returning updatedPaymentIds is just for integration test reason
     adding bank.call.fixedDelay property in the application.yml and @Scheduled to enable optimizing scheduler in production 
   
2. Introduce unit- and integration-tests;
   - adding PaymentServiceImplTest to **unit test** PaymentServiceImpl functionalities
     by testing addPayment and check the returned entity's all data
     and updateStatus when paymentId Not Founded
     and adding and updating payment status
   - adding scheduleRequestBank to JavaChallengeApplicationTests for **integration test** and ensure correct acting of system in interacting with banking api mock
        - fetching all empty bank payments in test platform
        - call the scheduleBankRequest and get updated payments
        - again fetching all empty bank payments in test platform
        - try to find conflict between new empty payments and updated payments returned by scheduleBankRequest
        - try to find conflict in updated payments that BankPaymentId field is null

3. Analyse and propose improvements if any are needed here; 
    - one simple improvement is adding index on bank_payment_id (index on status not preferred)
    - the very good improvement is using message queue (like Kafka) for storing and queueing payments wait to bank response

