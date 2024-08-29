import { useState } from "react";
import { SERVER_URL } from "../utils";
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
  Alert,
  AlertTitle,
  AlertIcon,
} from "@chakra-ui/react";

import { useNavigate } from "react-router-dom";

const Login = () => {
  const [user, setUser] = useState("");
  const [pass, setPass] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();
  const authenticate = async (route) => {
    if (!user || !pass) {
      return setError("Missing username or password.");
    }
    const response = await fetch(`${SERVER_URL}/api/${route}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({ user, pass }),
    });
    const data = await response.json();
    if (!data.success) {
      return setError(data.error);
    }
    navigate("/home");
  };

  return (
    <Flex
      minH={"100vh"}
      align={"center"}
      justify={"center"}
      bg={useColorModeValue("gray.50", "gray.800")}
    >
      <Stack spacing={8} mx={"auto"} py={12} px={6}>
        <Stack align={"center"}>
          <Heading fontSize={"4xl"}>Notes App 📋</Heading>
          <Text fontSize={"lg"} color={"gray.600"}>
            Login to post notes and view other people's notes ✌️
          </Text>
        </Stack>
        <Box
          rounded={"lg"}
          bg={useColorModeValue("white", "gray.700")}
          boxShadow={"lg"}
          p={8}
        >
          <Stack spacing={4}>
            <FormControl id="username">
              <FormLabel>Username</FormLabel>
              <Input
                name="username"
                type="text"
                onChange={(e) => setUser(e.target.value)}
                value={user}
              />
            </FormControl>
            <FormControl id="password">
              <FormLabel>Password</FormLabel>
              <Input
                name="password"
                type="password"
                onChange={(e) => setPass(e.target.value)}
                value={pass}
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
                onClick={async (e) => {
                  e && e.preventDefault();
                  await authenticate("login");
                }}
              >
                Sign in
              </Button>
            </Stack>
            <Stack spacing={10}>
              <Button
                onClick={(e) => {
                  e && e.preventDefault();
                  authenticate("register");
                }}
              >
                Register
              </Button>
            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
};

export default Login;
