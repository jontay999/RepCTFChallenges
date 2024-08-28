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
  FormControl,
  Input,
  Textarea,
  Alert,
  AlertIcon,
  AlertTitle,
} from "@chakra-ui/react";

import { SERVER_URL } from "../utils";
import { Link, useNavigate } from "react-router-dom";
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
      <Box p={4}>Main Content Here</Box>
      <Stack
        spacing={4}
        w="full"
        maxW="md"
        bg={useColorModeValue("gray.50", "gray.700")}
        rounded="xl"
        boxShadow="2xl"
        p={6}
        my={12}
      >
        <Heading lineHeight={1.1} fontSize={{ base: "2xl", md: "3xl" }}>
          Your Posts
        </Heading>
        <Stack alignItems="start">
          <ul>
            {posts.map((post, i) => (
              <Box key={i} ml={4}>
                <li style={{ textAlign: "left" }}>
                  <Button
                    variant="link"
                    as={Link}
                    to={`/post/${post.id}`}
                    justifyContent="start"
                  >
                    <Text fontSize={{ base: "md", md: "lg" }}>
                      {post.title}
                    </Text>
                  </Button>
                </li>
              </Box>
            ))}
          </ul>
        </Stack>
      </Stack>
    </>
  );
};

export default Home;
