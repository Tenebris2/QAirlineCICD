import { Box, Typography, Grid, Button, Divider, Stack } from "@mui/material";
import Header from "components/home-page/Header";
import Footer from "components/home-page/Footer";
import { useNavigate } from "react-router-dom";
import { ArrowBack, ArrowForward } from "@mui/icons-material";
import { useEffect, useState } from "react";
import { getAdverts } from "hooks/advert-hook";

const readMoreStyle = {
  position: "relative",
  display: "inline-block",
  cursor: "pointer",
  "&::after": {
    content: '""',
    position: "absolute",
    bottom: 0,
    left: 0,
    width: "100%",
    height: "2px",
    backgroundColor: "currentColor",
    transform: "scaleX(0)",
    transformOrigin: "bottom right",
    transition: "transform 0.3s ease",
  },
  "&:hover::after": {
    transform: "scaleX(1)",
    transformOrigin: "bottom left",
  },
};

const paginationStyle = {
  textTransform: "none",
  fontWeight: "500",
  color: "black",
  opacity: "0.6",
  transition: "opacity 0.3s ease, color 0.3s ease",
  "&:hover": {
    opacity: "1",
    color: "#1976d2",
    backgroundColor: "transparent",
  },
};

const titleStyle = {
  cursor: "pointer",
  transition: "color 0.3s ease",
  "&:hover": {
    color: "#1976d2",
  },
};

const PAGE_SIZE = 5;

const NewsList = () => {
  const navigate = useNavigate();
  const [currentPage, setCurrentPage] = useState(1);
  const [newsItems, setNewsItems] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const fetchedNews = await getAdverts();
        console.log("fetc", fetchedNews);
        const sortedNews = fetchedNews.sort(
          (a: any, b: any) => b.advert_id - a.advert_id
        );
        setNewsItems(sortedNews);
      } catch (error) {
        console.error("Error fetching news data", error);
      }
    };

    fetchNews();
  }, []);

  const sortedNews = [...newsItems].sort((a, b) => b.avert_id - a.advert_id);
  const totalPages = Math.ceil(newsItems.length / PAGE_SIZE);

  const paginatedNews = sortedNews.slice(
    (currentPage - 1) * PAGE_SIZE,
    currentPage * PAGE_SIZE
  );

  const goToPage = (page: number) => {
    if (page >= 1 && page <= totalPages) setCurrentPage(page);
  };

  useEffect(() => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }, [currentPage]);

  useEffect(() => {
    window.scrollTo({
      top: 0,
      behavior: "auto",
    });
  }, []);

  return (
    <Box>
      <Header />
      <Box sx={{ bgcolor: "rgb(242,244,247)" }}>
        <Box
          display="flex"
          alignItems="center"
          gap="10px"
          margin="auto"
          padding="20px 0"
          bgcolor="rgb(242,244,247)"
        >
          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: "10px",
              margin: "20px 80px 0",
              "@media (max-width: 1000px)": {
                margin: "0 20px 0",
              },
            }}
          >
            <i
              onClick={() => navigate("/")}
              className="fa-solid fa-house"
              style={{
                opacity: "0.6",
                transition: "opacity 0.3s ease, transform 0.3s ease",
                cursor: "pointer",
              }}
              onMouseEnter={(e) => (e.currentTarget.style.opacity = "1")}
              onMouseLeave={(e) => (e.currentTarget.style.opacity = "0.6")}
            ></i>
            <i
              className="fa-regular fa-greater-than"
              style={{
                opacity: "0.6",
              }}
            ></i>
            <Typography
              onClick={() => navigate("/")}
              variant="h6"
              sx={{
                opacity: 0.6,
                transition: "opacity 0.3s ease, text-decoration 0.3s ease",
                cursor: "pointer",
                "&:hover": {
                  opacity: 1,
                  textDecoration: "underline",
                },
              }}
            >
              QAirline
            </Typography>
            <i
              className="fa-regular fa-greater-than"
              style={{
                opacity: "0.6",
              }}
            ></i>
            <Typography
              onClick={() => goToPage(1)}
              variant="h6"
              sx={{
                opacity: 0.6,
                transition: "opacity 0.3s ease, text-decoration 0.3s ease",
                cursor: "pointer",
                "&:hover": {
                  opacity: 1,
                  textDecoration: "underline",
                },
              }}
            >
              News
            </Typography>
          </Box>
        </Box>
        <Box
          margin="0 80px 20px"
          sx={{
            "@media (max-width: 1000px)": {
              margin: "0 20px 0",
            },
          }}
        >
          <Typography variant="h4">News</Typography>
        </Box>
        <Box
          margin="20px 80px 20px"
          sx={{
            "@media (max-width: 1000px)": {
              margin: "20px 20px 0",
            },
          }}
        >
          <Grid container spacing={3}>
            <Grid item xs={12}>
              <Box>
                <Box
                  sx={{
                    width: "100%",
                    height: "368px",
                    overflow: "hidden",
                    borderRadius: "10px",
                  }}
                >
                  <img
                    onClick={() =>
                      navigate(`/news/new/${paginatedNews[0]?.advert_id}`)
                    }
                    src={paginatedNews[0]?.media_link}
                    alt={paginatedNews[0]?.advert_name}
                    style={{
                      height: "368px",
                      width: "100%",
                      objectFit: "cover",
                      borderRadius: "10px",
                      cursor: "pointer",
                      transition: "transform 0.3s ease-in-out",
                    }}
                    onMouseEnter={(e) =>
                      (e.currentTarget.style.transform = "scale(1.1)")
                    }
                    onMouseLeave={(e) =>
                      (e.currentTarget.style.transform = "scale(1)")
                    }
                  />
                </Box>
                <Box mt={2}>
                  <Typography
                    onClick={() =>
                      navigate(`/news/new/${paginatedNews[0]?.advert_id}`)
                    }
                    variant="h5"
                    sx={titleStyle}
                  >
                    {paginatedNews[0]?.advert_name}
                  </Typography>
                  <Typography
                    onClick={() =>
                      navigate(`/news/new/${paginatedNews[0]?.advert_id}`)
                    }
                    variant="h6"
                    color="primary"
                    sx={readMoreStyle}
                  >
                    Read More
                  </Typography>
                </Box>
              </Box>
            </Grid>
            {paginatedNews.slice(1).map((news) => (
              <Grid item xs={12} md={6} key={news.advert_name}>
                <Box>
                  <Box
                    sx={{
                      width: "100%",
                      height: "368px",
                      overflow: "hidden",
                      borderRadius: "10px",
                    }}
                  >
                    <img
                      onClick={() => navigate(`/news/new/${news?.advert_id}`)}
                      src={news.media_link}
                      alt={news.advert_name}
                      style={{
                        height: "368px",
                        width: "100%",
                        objectFit: "cover",
                        borderRadius: "10px",
                        cursor: "pointer",
                        transition: "transform 0.3s ease-in-out",
                      }}
                      onMouseEnter={(e) =>
                        (e.currentTarget.style.transform = "scale(1.1)")
                      }
                      onMouseLeave={(e) =>
                        (e.currentTarget.style.transform = "scale(1)")
                      }
                    />
                  </Box>
                  <Typography
                    variant="h5"
                    sx={titleStyle}
                    marginTop="16px"
                    onClick={() => navigate(`/news/new/${news?.advert_id}`)}
                  >
                    {news.advert_name}
                  </Typography>
                  <Typography
                    variant="h6"
                    color="primary"
                    sx={readMoreStyle}
                    onClick={() => navigate(`/news/new/${news?.advert_id}`)}
                  >
                    Read More
                  </Typography>
                </Box>
              </Grid>
            ))}
          </Grid>
        </Box>

        {/* Pagination */}
        <Box margin="20px 80px">
          <Divider />
          <Stack
            direction="row"
            justifyContent="center"
            spacing={2}
            padding="20px 0"
          >
            <Button
              disableRipple
              onClick={() => goToPage(1)}
              sx={paginationStyle}
              startIcon={<ArrowBack />}
            >
              First
            </Button>
            <Button
              disableRipple
              onClick={() => goToPage(currentPage - 1)}
              sx={paginationStyle}
            >
              Previous
            </Button>
            <Box>
              <Typography fontSize="1.2rem">
                Page {currentPage} of {totalPages}
              </Typography>
            </Box>

            <Button
              disableRipple
              onClick={() => goToPage(currentPage + 1)}
              sx={paginationStyle}
            >
              Next
            </Button>
            <Button
              disableRipple
              onClick={() => goToPage(totalPages)}
              sx={paginationStyle}
              endIcon={<ArrowForward />}
            >
              Last
            </Button>
          </Stack>
        </Box>
      </Box>
      <Footer />
    </Box>
  );
};

export default NewsList;
