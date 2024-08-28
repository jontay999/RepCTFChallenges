import { useState, useEffect } from "react";
import { SERVER_URL } from "../utils";
import {
  Box,
  Heading,
  Button,
  Stack,
  useColorModeValue,
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
    <Box
      rounded={"lg"}
      bg={useColorModeValue("white", "gray.700")}
      boxShadow={"lg"}
      p={8}
    >
      <Stack spacing={4}></Stack>
      <Heading>Title: {title}</Heading>
      <div>Content: {content}</div>
      <Button variant="link" as={Link} to="/home" my={4}>
        Back
      </Button>
    </Box>
  );
};

export default ViewPost;
