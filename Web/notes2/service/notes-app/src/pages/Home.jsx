import { useEffect, useState } from "react";
import Header from "../components/Header";
import {
  Box,
  Heading,
  Text,
  Button,
  Stack,
  useColorModeValue,
  Flex,
} from "@chakra-ui/react";

import { SERVER_URL } from "../utils";
import { Link, useNavigate } from "react-router-dom";
import CreatePost from "../components/CreatePost";
const Home = () => {
  const [posts, setPosts] = useState([]);
  const navigate = useNavigate();

  const fetch_posts = async () => {
    const response = await fetch(`${SERVER_URL}/api/posts`, {
      credentials: "include",
      method: "POST",
    });
    const data = await response.json();
    if (!data.success) {
      return navigate("/");
    }
    setPosts(data.data);
  };
  useEffect(() => {
    fetch_posts();
  }, []);

  return (
    <>
      <Header />
      <Flex width={"100%"} justifyContent={"center"}>
        <CreatePost callback={fetch_posts} />
        <Stack flex={1} spacing={8} py={12} px={6}>
          <Box
            rounded={"lg"}
            bg={useColorModeValue("white", "gray.700")}
            boxShadow={"lg"}
            p={8}
          >
            <Heading>Your Posts 📔</Heading>
            <Stack alignItems="start" p={8}>
              <ul>
                {posts.length === 0 ? (
                  <Text>No posts yet.</Text>
                ) : (
                  posts.map((post, i) => (
                    <Box key={i} ml={4}>
                      <li style={{ textAlign: "left" }}>
                        <Box justifyContent="start">
                          <Text fontWeight="bold">{post.title}: </Text>
                          <Text ml={1}>{post.content}</Text>
                        </Box>
                      </li>
                    </Box>
                  ))
                )}
              </ul>
            </Stack>
          </Box>
        </Stack>
      </Flex>
    </>
  );
};

export default Home;
