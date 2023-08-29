--
-- PostgreSQL database dump
--

-- Dumped from database version 14.9 (Homebrew)
-- Dumped by pg_dump version 14.9 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bot_responces; Type: TABLE; Schema: public; Owner: ronney
--

CREATE TABLE public.bot_responces (
    "Date" timestamp without time zone,
    user_question text,
    bot_response text
);


ALTER TABLE public.bot_responces OWNER TO ronney;

--
-- Data for Name: bot_responces; Type: TABLE DATA; Schema: public; Owner: ronney
--

COPY public.bot_responces ("Date", user_question, bot_response) FROM stdin;
2023-08-29 09:34:02.894716	hi	I am a chatbot.
2023-08-29 09:56:05.91333	Hi	I am a chatbot.
2023-08-29 09:56:11.189146	project	Hey, Please Share your Project Title.
2023-08-29 09:56:15.657601	social media	Nice, you can go with mobile application with android or for cross platform flutter or react native would be good idea
2023-08-29 09:57:15.301577	library	Nice you can go with desktop application with .net or java
2023-08-29 09:58:00.847955	snapchat	Nice you can go with mobile application with android or for cross platform flutter or react native would be good idea
2023-08-29 10:16:09.905377	hi	I am a chatbot.
2023-08-29 10:16:19.374645	need help for project	Hey, Please Share your Project Title.
2023-08-29 10:16:23.652663	social media	Nice, you can go with mobile application with android or for cross platform flutter or react native would be good idea
\.


--
-- PostgreSQL database dump complete
--

