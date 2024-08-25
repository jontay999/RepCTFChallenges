import * as React from "react";
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

import { useNavigate, Link } from "react-router-dom";

export default function SimpleCard() {
  const [user, setUser] = React.useState("");
  const [pass, setPass] = React.useState("");
  const [error, setError] = React.useState("");

  const navigate = useNavigate();
  const login = async (e) => {
    e && e.preventDefault();
    if (!user || !pass) {
      return setError("Missing username or password.");
    }
    fetch(`${SERVER_URL}/api/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user, pass }),
    })
      .then((r) => r.json())
      .then((resp) => {
        if (!resp.success) {
          return setError(resp.error);
        }
        navigate("/home");
      });
  };

  return (
    <Flex
      minH={"100vh"}
      align={"center"}
      justify={"center"}
      bg={useColorModeValue("gray.50", "gray.800")}
    >
      <Stack spacing={8} mx={"auto"} maxW={"lg"} py={12} px={6}>
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
                onClick={login}
              >
                Sign in
              </Button>
            </Stack>
            <Stack spacing={10}>
              <Button variant="link" as={Link} to="/register">
                Register
              </Button>
            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
}
