import * as React from "react";
import Header from "../components/Header";
import {
  Box,
  Heading,
  Container,
  Text,
  Button,
  Stack,
  useColorModeValue,
  Flex,
  FormControl,
  Input,
  Textarea,
  Alert,
  AlertIcon,
  AlertTitle,
} from "@chakra-ui/react";

import { SERVER_URL } from "../utils";
import { Link, useNavigate } from "react-router-dom";
import CreatePost from "../components/CreatePost";
const Home = () => {
  const [posts, setPosts] = React.useState([]);
  const navigate = useNavigate();

  const fetchPosts = () => {
    fetch(`${SERVER_URL}/api/posts`, { credentials: "include", method: "POST" })
      .then((r) => r.json())
      .then((resp) => {
        console.log("resp:", resp);
        if (!resp.success) {
          return navigate("/");
        }
        setPosts(resp.data);
        console.log("got posts");
      });
  };
  React.useEffect(fetchPosts, [navigate]);

  return (
    <>
      <Header />
      <Flex width={"100%"} justifyContent={"center"}>
        <CreatePost />
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
                        <Button
                          variant="link"
                          as={Link}
                          to={`/post/${post.id}`}
                          justifyContent="start"
                        >
                          <Text>{post.title}</Text>
                        </Button>
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
