import { useState } from "react";
import Header from "../components/Header";
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

const sample_results = [
  { title: "title1", content: "content1" },
  { title: "title2", content: "content2" },
  { title: "title3", content: "content3" },
];
const Search = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [error, setError] = useState("");

  const search = async (e) => {
    e.preventDefault();
    if (!query) {
      return setError("Query cannot be empty!");
    }
    const response = await fetch(`${SERVER_URL}/api/search/${query}`, {
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
    });
    const data = await response.json();
    setResults(data.results);
  };

  return (
    <Box minHeight={"100vh"} bg={useColorModeValue("gray.50", "gray.800")}>
      <Header />
      <Flex align={"center"} justify={"center"}>
        <Stack spacing={8} mx={"auto"} py={12} px={6}>
          <Stack align={"center"}>
            <Heading fontSize={"4xl"}>
              Search for notes based on content! 🔍
            </Heading>
            <Text fontSize={"lg"} color={"gray.600"}>
              (Of course, you can only view your own notes!)
            </Text>
          </Stack>
          <Box
            rounded={"lg"}
            bg={useColorModeValue("white", "gray.700")}
            boxShadow={"lg"}
            p={8}
          >
            <Stack spacing={4}>
              <FormControl id="query">
                <FormLabel>Query</FormLabel>
                <Input
                  name="query"
                  type="text"
                  onChange={(e) => setQuery(e.target.value)}
                  value={query}
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
                  onClick={search}
                >
                  Search
                </Button>
              </Stack>
            </Stack>
          </Box>
          <Box
            rounded={"lg"}
            bg={useColorModeValue("white", "gray.700")}
            boxShadow={"lg"}
            p={8}
          >
            <Stack spacing={4}>
              <Heading fontSize={"2xl"}>Results</Heading>
              <Stack alignItems="start" p={8}>
                <ul>
                  {results.length === 0 ? (
                    <Text>No results.</Text>
                  ) : (
                    results.map((result, i) => (
                      <Box key={i} ml={4}>
                        <li style={{ textAlign: "left" }}>
                          <Text fontWeight="bold">{result.title}: </Text>
                          <Text ml={1}>{result.content}</Text>
                        </li>
                      </Box>
                    ))
                  )}
                </ul>
              </Stack>
            </Stack>
          </Box>
        </Stack>
      </Flex>
    </Box>
  );
};

export default Search;
