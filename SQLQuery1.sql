create database uber;

use uber;

---------------------------------------------------------------------------

drop table if exists rides;

CREATE TABLE rides (
    Date DATE,
    Time TIME,
    Booking_ID VARCHAR(20),
    Booking_Status VARCHAR(50),
    Customer_ID VARCHAR(20),
    Vehicle_Type VARCHAR(50),
    Pickup_Location VARCHAR(100),
    Drop_Location VARCHAR(100),

    Cancelled_Rides_by_Customer INT,
    Reason_for_cancelling_by_Customer VARCHAR(255),

    Cancelled_Rides_by_Driver INT,
    Driver_Cancellation_Reason VARCHAR(255),

    Incomplete_Rides INT,
    Incomplete_Rides_Reason VARCHAR(255),

    Booking_Value INT,
    Ride_Distance INT,

    Driver_Ratings INT,
    Customer_Rating INT,

    Payment_Method VARCHAR(50)
);


drop table if exists vehicles;

CREATE TABLE vehicles (
    Vehicle_Type VARCHAR(50),
    Image_URL VARCHAR(500)
);


----------------------------------------------------------------------------------------


select * from rides
select * from vehicles



ALTER TABLE dbo.rides
ALTER COLUMN [Date] DATE;

select MAX(Date) as Latest_Ride_Date from dbo.rides
select MIN(Date) as Earliest_Ride_Date from dbo.rides

ALTER TABLE dbo.rides
ALTER COLUMN [Time] TIME(0);

ALTER TABLE dbo.rides
ALTER COLUMN [Cancelled Rides by Customer] INT;

ALTER TABLE dbo.rides
ALTER COLUMN [Cancelled Rides by Driver] INT;

ALTER TABLE dbo.rides
ALTER COLUMN [Incomplete Rides] INT;

ALTER TABLE dbo.rides
ALTER COLUMN [Booking Value] INT;

ALTER TABLE dbo.rides
ALTER COLUMN [Ride Distance] DECIMAL(10,2);

ALTER TABLE dbo.rides
ALTER COLUMN [Driver Ratings] DECIMAL(3,2);

ALTER TABLE dbo.rides
ALTER COLUMN [Customer Rating] DECIMAL(3,2);




select * from rides
select * from vehicles