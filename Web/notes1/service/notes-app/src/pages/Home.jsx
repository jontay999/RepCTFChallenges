import * as React from "react";
import Header from "../components/Header";
import { Box } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
const Home = () => {
  const [posts, setPosts] = React.useState([]);
  const navigate = useNavigate();

  const fetchPosts = () => {
    fetch("/api/posts", { method: "POST" })
      .then((r) => r.json())
      .then((resp) => {
        if (!resp.success) {
          return navigate("/");
        }
        setPosts(resp.data);
      });
  };
  React.useEffect(fetchPosts, [navigate]);

  return (
    <>
      <Header />
      <Box p={4}>Main Content Here</Box>
    </>
  );
};

export default Home;
