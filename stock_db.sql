/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2017/6/21 23:37:23                           */
/*==============================================================*/


drop table if exists Stock_Company;

drop table if exists Stock_Info;

drop table if exists Stock_Type;

/*==============================================================*/
/* Table: Stock_Company                                         */
/*==============================================================*/
create table Stock_Company
(
   SCID                 int not null auto_increment,
   SCNAME               varchar(100),
   primary key (SCID)
);

/*==============================================================*/
/* Table: Stock_Info                                            */
/*==============================================================*/
create table Stock_Info
(
   ID                   int not null auto_increment,
   GPJYM                varchar(10),
   GPMC                 varchar(100),
   STID                 int,
   SCID                 int,
   JYR                  datetime,
   SPJG                 double,
   JKJG                 double,
   SJJG                 double,
   CJL                  double,
   HSL                  double,
   ZGJG                 double,
   ZDJG                 double,
   ZTJG                 double,
   DTJG                 double,
   NP                   double,
   WP                   double,
   CJE                  double,
   ZF                   double,
   WB                   double,
   LB                   double,
   LTSZ                 double,
   ZSZ                  double,
   SYL                  double,
   SJL                  double,
   MGSY                 double,
   MGJZC                double,
   ZGB                  double,
   LTGB                 double,
   ZLLRL                decimal,
   ZLLRZ                double,
   ZLLCL                decimal,
   ZLLCZ                double,
   SHLRL                decimal,
   SHLRZ                double,
   SHLCL                decimal,
   SHLCZ                double,
   primary key (ID)
);

/*==============================================================*/
/* Table: Stock_Type                                            */
/*==============================================================*/
create table Stock_Type
(
   STID                 int not null auto_increment,
   STNAME               varchar(100),
   primary key (STID)
);

alter table Stock_Info add constraint FK_Stock_Company_Reference foreign key (SCID)
      references Stock_Company (SCID) on delete restrict on update restrict;

alter table Stock_Info add constraint FK_Ttock_Type_Reference foreign key (STID)
      references Stock_Type (STID) on delete restrict on update restrict;

insert into Stock_Company(SCNAME) values('上海股票');
insert into Stock_Company(SCNAME) values('深圳股票');
	  
insert into Stock_Type(STNAME) values('沪市A股');
insert into Stock_Type(STNAME) values('深市A股');
insert into Stock_Type(STNAME) values('沪市新股申购');
insert into Stock_Type(STNAME) values('深市新股申购');
insert into Stock_Type(STNAME) values('沪市配股');
insert into Stock_Type(STNAME) values('深市配股');
insert into Stock_Type(STNAME) values('中小板');
insert into Stock_Type(STNAME) values('创业板');