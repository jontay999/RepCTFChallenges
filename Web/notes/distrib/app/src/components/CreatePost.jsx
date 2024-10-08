import { useState } from "react";
import { SERVER_URL } from "../utils";
import {
  Button,
  Alert,
  AlertIcon,
  AlertTitle,
  Input,
  Stack,
  FormControl,
  FormLabel,
  Heading,
  Box,
  useColorModeValue,
} from "@chakra-ui/react";

const CreatePost = ({ callback }) => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [error, setError] = useState("");

  const submit = async (e) => {
    e.preventDefault();
    if (!title || !content) {
      return setError("Missing content or title.");
    }
    const response = await fetch(`${SERVER_URL}/api/create`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({
        title,
        content,
      }),
    });
    const data = await response.json();
    if (!data.success) {
      return setError(data.error);
    }
    setTitle("");
    setContent("");
    setError("");
    callback();
  };

  return (
    <Stack flex={1} spacing={8} py={12} px={6}>
      <Box
        rounded={"lg"}
        bg={useColorModeValue("white", "gray.700")}
        boxShadow={"lg"}
        p={8}
      >
        <Stack spacing={4}>
          <Stack align={"center"}>
            <Heading fontSize={"4xl"}>Create a Post ✍️</Heading>
          </Stack>
          <FormControl id="title">
            <FormLabel>Title</FormLabel>
            <Input
              name="title"
              type="text"
              onChange={(e) => setTitle(e.target.value)}
              value={title}
            />
          </FormControl>
          <FormControl id="content">
            <FormLabel>Content</FormLabel>
            <Input
              name="content"
              type="text"
              onChange={(e) => setContent(e.target.value)}
              value={content}
            />
          </FormControl>
          {error && (
            <Alert status="error" variant="solid">
              <AlertIcon />
              <AlertTitle>{error}</AlertTitle>
            </Alert>
          )}
          <Stack spacing={10}>
            <Button
              bg={"blue.400"}
              color={"white"}
              _hover={{
                bg: "blue.500",
              }}
              onClick={submit}
            >
              Create
            </Button>
          </Stack>
        </Stack>
      </Box>
    </Stack>
  );
};

export default CreatePost;
