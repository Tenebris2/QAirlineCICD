import {
    Box,
    Typography,
    Radio,
    FormControlLabel,
    RadioGroup,
    Collapse,
} from "@mui/material";
import {usePaymentStore} from "hooks/payment-hook"; // Import the payment store

const Payment = () => {
    const {paymentOption, setPaymentOption} = usePaymentStore();

    const handlePaymentChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setPaymentOption(event.target.value); // Update the payment option in the store
        console.log(event.target.value)
    };


    return (
        <Box
            sx={{
                backgroundColor: "white",
                borderRadius: "20px",
                padding: "20px",
                color: "black",
                boxShadow: "0px 4px 20px rgba(0, 0, 0, 0.1)",
                display: "flex",
                flexDirection: "column",
                gap: "24px",
                marginTop: "40px",
            }}
        >
            <Typography variant="h6">How would you like to pay?</Typography>
            <RadioGroup
                value={paymentOption}
                onChange={handlePaymentChange}
                sx={{display: "flex", flexDirection: "column", gap: "16px"}}
            >
                <FormControlLabel
                    value="payLater"
                    control={<Radio color="primary"/>}
                    label="Pay Later"
                />
                <FormControlLabel
                    value="payNow"
                    control={<Radio color="primary"/>}
                    label="Pay Now"
                />
                <Collapse in={paymentOption === "payNow"}>
                    <Box
                        sx={{
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "center",
                            padding: "16px",
                            backgroundColor: "#f5f5f5",
                            borderRadius: "12px",
                        }}
                    >
                        <img src="/qr.png" alt="QR code for flight booking"/>
                    </Box>
                </Collapse>
            </RadioGroup>
            {/* <TextField
          fullWidth
          label="Booker Email*"
          value={bookerEmail}
          onChange={(e) => handleBookerEmailField(e.target.value)}
          variant="outlined"
        /> */}
        </Box>
    );
};

export default Payment;
