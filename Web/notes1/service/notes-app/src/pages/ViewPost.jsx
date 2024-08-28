import { useState, useEffect } from "react";
import { SERVER_URL } from "../utils";
import {
  Box,
  Heading,
  Button,
  Stack,
  useColorModeValue,
  Flex,
} from "@chakra-ui/react";
import { Link, useParams, useNavigate } from "react-router-dom";

const ViewPost = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const navigate = useNavigate();
  const { id } = useParams();

  const get_post = async () => {
    const response = await fetch(
      `${SERVER_URL}/api/post/` + encodeURIComponent(id),
      {
        method: "GET",
        credentials: "include",
      }
    );
    const data = await response.json();
    if (!data.success) {
      return navigate("/home");
    }
    setTitle(data.data.title);
    setContent(data.data.content);
  };

  useEffect(() => {
    get_post();
  }, []);

  return (
    <Flex
      minH={"100vh"}
      align={"center"}
      justify={"center"}
      bg={useColorModeValue("gray.50", "gray.800")}
    >
      <Box
        minW={400}
        rounded={"lg"}
        bg={useColorModeValue("white", "gray.700")}
        boxShadow={"lg"}
        p={24}
        mx={12}
        my={8}
      >
        <Stack spacing={4}>
          <Heading>{title}</Heading>
          <div>{content}</div>
          <Button variant="link" as={Link} to="/home" my={4}>
            Back
          </Button>
        </Stack>
      </Box>
    </Flex>
  );
};

export default ViewPost;
